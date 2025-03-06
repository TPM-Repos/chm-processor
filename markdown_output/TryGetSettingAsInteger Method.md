       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetSettingAsInteger Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic461.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISettingsManager Interface](topic442.md) : TryGetSettingAsInteger Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_level_
    The level from which to load the setting.

_settingName_
    The full name of the setting, e.g. "Common\MyValue".

_preventRedirection_
    True to prevent automatic redirection if redirection is turned on.

_value_
    Receives the value of the setting.

Glossary Item Box

Gets the specified setting as a boolean. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TryGetSettingAsInteger( _
       ByVal _level_ As [SettingLevel](topic661.md), _
       ByVal _settingName_ As String, _
       ByVal _preventRedirection_ As Boolean, _
       ByRef _value_ As Integer _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISettingsManager](topic442.md)
    Dim level As [SettingLevel](topic661.md)
    Dim settingName As String
    Dim preventRedirection As Boolean
    Dim value As Integer
    Dim value As Boolean
     
    value = instance.TryGetSettingAsInteger(level, settingName, preventRedirection, value)  
  
C#|   
---|---  
      
    
    bool TryGetSettingAsInteger( 
       [SettingLevel](topic661.md) _level_ ,
       string _settingName_ ,
       bool _preventRedirection_ ,
       out int _value_
    )  
  
#### Parameters

 _level_
    The level from which to load the setting.
_settingName_
    The full name of the setting, e.g. "Common\MyValue".
_preventRedirection_
    True to prevent automatic redirection if redirection is turned on.
_value_
    Receives the value of the setting.

#### Return Value

True if the setting was retrieved, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISettingsManager Interface](topic442.md)   
[ISettingsManager Members](topic443.md)

©2024 DriveWorks Ltd. All Rights Reserved.
