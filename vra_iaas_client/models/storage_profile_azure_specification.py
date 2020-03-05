# coding: utf-8

"""
    VMware Cloud Assembly IaaS API

    A multi-cloud IaaS API for Cloud Automation Services  # noqa: E501

    OpenAPI spec version: 2019-01-15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StorageProfileAzureSpecification(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'storage_account_id': 'str',
        'supports_encryption': 'bool',
        'region_id': 'str',
        'name': 'str',
        'description': 'str',
        'default_item': 'bool',
        'disk_type': 'str',
        'data_disk_caching': 'str',
        'os_disk_caching': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'storage_account_id': 'storageAccountId',
        'supports_encryption': 'supportsEncryption',
        'region_id': 'regionId',
        'name': 'name',
        'description': 'description',
        'default_item': 'defaultItem',
        'disk_type': 'diskType',
        'data_disk_caching': 'dataDiskCaching',
        'os_disk_caching': 'osDiskCaching',
        'tags': 'tags'
    }

    def __init__(self, storage_account_id=None, supports_encryption=None, region_id=None, name=None, description=None, default_item=None, disk_type=None, data_disk_caching=None, os_disk_caching=None, tags=None):  # noqa: E501
        """StorageProfileAzureSpecification - a model defined in Swagger"""  # noqa: E501

        self._storage_account_id = None
        self._supports_encryption = None
        self._region_id = None
        self._name = None
        self._description = None
        self._default_item = None
        self._disk_type = None
        self._data_disk_caching = None
        self._os_disk_caching = None
        self._tags = None
        self.discriminator = None

        if storage_account_id is not None:
            self.storage_account_id = storage_account_id
        if supports_encryption is not None:
            self.supports_encryption = supports_encryption
        self.region_id = region_id
        self.name = name
        if description is not None:
            self.description = description
        if default_item is not None:
            self.default_item = default_item
        if disk_type is not None:
            self.disk_type = disk_type
        if data_disk_caching is not None:
            self.data_disk_caching = data_disk_caching
        if os_disk_caching is not None:
            self.os_disk_caching = os_disk_caching
        if tags is not None:
            self.tags = tags

    @property
    def storage_account_id(self):
        """Gets the storage_account_id of this StorageProfileAzureSpecification.  # noqa: E501

        Id of a storage account where in the disk is placed.  # noqa: E501

        :return: The storage_account_id of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._storage_account_id

    @storage_account_id.setter
    def storage_account_id(self, storage_account_id):
        """Sets the storage_account_id of this StorageProfileAzureSpecification.

        Id of a storage account where in the disk is placed.  # noqa: E501

        :param storage_account_id: The storage_account_id of this StorageProfileAzureSpecification.  # noqa: E501
        :type: str
        """

        self._storage_account_id = storage_account_id

    @property
    def supports_encryption(self):
        """Gets the supports_encryption of this StorageProfileAzureSpecification.  # noqa: E501

        Indicates whether this storage policy should support encryption or not.  # noqa: E501

        :return: The supports_encryption of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._supports_encryption

    @supports_encryption.setter
    def supports_encryption(self, supports_encryption):
        """Sets the supports_encryption of this StorageProfileAzureSpecification.

        Indicates whether this storage policy should support encryption or not.  # noqa: E501

        :param supports_encryption: The supports_encryption of this StorageProfileAzureSpecification.  # noqa: E501
        :type: bool
        """

        self._supports_encryption = supports_encryption

    @property
    def region_id(self):
        """Gets the region_id of this StorageProfileAzureSpecification.  # noqa: E501

        The If of the region that is associated with the storage profile.  # noqa: E501

        :return: The region_id of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this StorageProfileAzureSpecification.

        The If of the region that is associated with the storage profile.  # noqa: E501

        :param region_id: The region_id of this StorageProfileAzureSpecification.  # noqa: E501
        :type: str
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def name(self):
        """Gets the name of this StorageProfileAzureSpecification.  # noqa: E501

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :return: The name of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageProfileAzureSpecification.

        A human-friendly name used as an identifier in APIs that support this option.  # noqa: E501

        :param name: The name of this StorageProfileAzureSpecification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this StorageProfileAzureSpecification.  # noqa: E501

        A human-friendly description.  # noqa: E501

        :return: The description of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StorageProfileAzureSpecification.

        A human-friendly description.  # noqa: E501

        :param description: The description of this StorageProfileAzureSpecification.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def default_item(self):
        """Gets the default_item of this StorageProfileAzureSpecification.  # noqa: E501

        Indicates if a storage policy contains default storage properties.  # noqa: E501

        :return: The default_item of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._default_item

    @default_item.setter
    def default_item(self, default_item):
        """Sets the default_item of this StorageProfileAzureSpecification.

        Indicates if a storage policy contains default storage properties.  # noqa: E501

        :param default_item: The default_item of this StorageProfileAzureSpecification.  # noqa: E501
        :type: bool
        """

        self._default_item = default_item

    @property
    def disk_type(self):
        """Gets the disk_type of this StorageProfileAzureSpecification.  # noqa: E501

        Indicates the performance tier for the storage type. Premium disks are SSD backed and Standard disks are HDD backed.  # noqa: E501

        :return: The disk_type of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this StorageProfileAzureSpecification.

        Indicates the performance tier for the storage type. Premium disks are SSD backed and Standard disks are HDD backed.  # noqa: E501

        :param disk_type: The disk_type of this StorageProfileAzureSpecification.  # noqa: E501
        :type: str
        """

        self._disk_type = disk_type

    @property
    def data_disk_caching(self):
        """Gets the data_disk_caching of this StorageProfileAzureSpecification.  # noqa: E501

        Indicates the caching mechanism for additional disk.   # noqa: E501

        :return: The data_disk_caching of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._data_disk_caching

    @data_disk_caching.setter
    def data_disk_caching(self, data_disk_caching):
        """Sets the data_disk_caching of this StorageProfileAzureSpecification.

        Indicates the caching mechanism for additional disk.   # noqa: E501

        :param data_disk_caching: The data_disk_caching of this StorageProfileAzureSpecification.  # noqa: E501
        :type: str
        """

        self._data_disk_caching = data_disk_caching

    @property
    def os_disk_caching(self):
        """Gets the os_disk_caching of this StorageProfileAzureSpecification.  # noqa: E501

        Indicates the caching mechanism for OS disk. Default policy for OS disks is Read/Write.  # noqa: E501

        :return: The os_disk_caching of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: str
        """
        return self._os_disk_caching

    @os_disk_caching.setter
    def os_disk_caching(self, os_disk_caching):
        """Sets the os_disk_caching of this StorageProfileAzureSpecification.

        Indicates the caching mechanism for OS disk. Default policy for OS disks is Read/Write.  # noqa: E501

        :param os_disk_caching: The os_disk_caching of this StorageProfileAzureSpecification.  # noqa: E501
        :type: str
        """

        self._os_disk_caching = os_disk_caching

    @property
    def tags(self):
        """Gets the tags of this StorageProfileAzureSpecification.  # noqa: E501

        A set of tag keys and optional values for a storage policy which define set of specifications for creating a disk.  # noqa: E501

        :return: The tags of this StorageProfileAzureSpecification.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this StorageProfileAzureSpecification.

        A set of tag keys and optional values for a storage policy which define set of specifications for creating a disk.  # noqa: E501

        :param tags: The tags of this StorageProfileAzureSpecification.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(StorageProfileAzureSpecification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StorageProfileAzureSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other