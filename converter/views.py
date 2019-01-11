from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.scraper_utils import get_exchange_rate
from .utils.exchange_calculator import calculate_exchange
from rest_framework import status
from .constants import api_constants


class ConverterView(APIView):
    """
    View to handle currency conversion operations 
    """

    def get(self, request, format=None):
        try:
            # Obtaining query params
            source_type = request.query_params.get(api_constants.SOURCE)
            target_type = request.query_params.get(api_constants.TARGET)
            amount = request.query_params.get(api_constants.AMOUNT)

            # Initialising variables here so that error handling can be done using the same variables
            conversion_rate = None
            converted_amount = None
            data = {}

            # Checking whether all query params are supplied
            if source_type and target_type and amount:
                conversion_rate = get_exchange_rate(source_type, target_type)

                # Checking if data was scraped correctly and whether conversion rate was obtained
                if conversion_rate:
                    converted_amount = calculate_exchange(
                        float(amount), conversion_rate)
                else:
                    return Response(api_constants.EXCHANGE_RATE_ERROR.format(source_type, target_type), status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(api_constants.WRONG_PARAMS, status=status.HTTP_400_BAD_REQUEST)

            # Returning response in JSON format
            if converted_amount:
                data[api_constants.SOURCE_CURRENCY] = source_type
                data[api_constants.TARGET_CURRENCY] = target_type
                data[api_constants.SOURCE_AMOUNT] = amount
                data[api_constants.CONVERTED_AMOUNT] = converted_amount
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(api_constants.UNEXPECTED_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as exc:
            return Response(api_constants.UNEXPECTED_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
