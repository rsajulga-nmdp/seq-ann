# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Feature(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, locus=None, term=None, rank=None, accession=None, sequence=None, hash_code=None):
        """
        Feature - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'locus': 'str',
            'term': 'str',
            'rank': 'int',
            'accession': 'int',
            'sequence': 'str',
            'hash_code': 'int'
        }

        self.attribute_map = {
            'locus': 'locus',
            'term': 'term',
            'rank': 'rank',
            'accession': 'accession',
            'sequence': 'sequence',
            'hash_code': 'hashCode'
        }

        self._locus = locus
        self._term = term
        self._rank = rank
        self._accession = accession
        self._sequence = sequence
        self._hash_code = hash_code

    @property
    def locus(self):
        """
        Gets the locus of this Feature.


        :return: The locus of this Feature.
        :rtype: str
        """
        return self._locus

    @locus.setter
    def locus(self, locus):
        """
        Sets the locus of this Feature.


        :param locus: The locus of this Feature.
        :type: str
        """

        self._locus = locus

    @property
    def term(self):
        """
        Gets the term of this Feature.


        :return: The term of this Feature.
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """
        Sets the term of this Feature.


        :param term: The term of this Feature.
        :type: str
        """

        self._term = term

    @property
    def rank(self):
        """
        Gets the rank of this Feature.


        :return: The rank of this Feature.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """
        Sets the rank of this Feature.


        :param rank: The rank of this Feature.
        :type: int
        """

        self._rank = rank

    @property
    def accession(self):
        """
        Gets the accession of this Feature.


        :return: The accession of this Feature.
        :rtype: int
        """
        return self._accession

    @accession.setter
    def accession(self, accession):
        """
        Sets the accession of this Feature.


        :param accession: The accession of this Feature.
        :type: int
        """

        self._accession = accession

    @property
    def sequence(self):
        """
        Gets the sequence of this Feature.


        :return: The sequence of this Feature.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """
        Sets the sequence of this Feature.


        :param sequence: The sequence of this Feature.
        :type: str
        """

        self._sequence = sequence

    @property
    def hash_code(self):
        """
        Gets the hash_code of this Feature.


        :return: The hash_code of this Feature.
        :rtype: int
        """
        return self._hash_code

    @hash_code.setter
    def hash_code(self, hash_code):
        """
        Sets the hash_code of this Feature.


        :param hash_code: The hash_code of this Feature.
        :type: int
        """

        self._hash_code = hash_code

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
