       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetSettingEncrypted Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic826.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [Extensions Class](topic814.md) : SetSettingEncrypted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_this_
    The [ISettingsManager](topic442.md) to use to save the specified setting.

_level_
    The level at which to save the setting.

_settingName_
    The full name of the setting, e.g. "Common\MyValue".

_settingValue_
    The value to save.

_preventRedirection_
    True to prevent automatic redirection if redirection is turned on.

Glossary Item Box

Saves the specified setting. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <ExtensionAttribute()>
    Public Shared Sub SetSettingEncrypted( _
       ByVal _this_ As [ISettingsManager](topic442.md), _
       ByVal _level_ As [SettingLevel](topic661.md), _
       ByVal _settingName_ As String, _
       ByVal _settingValue_ As String, _
       ByVal _preventRedirection_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim this As [ISettingsManager](topic442.md)
    Dim level As [SettingLevel](topic661.md)
    Dim settingName As String
    Dim settingValue As String
    Dim preventRedirection As Boolean
     
    [Extensions](topic814.md).SetSettingEncrypted(this, level, settingName, settingValue, preventRedirection)  
  
C#|   
---|---  
      
    
    [ExtensionAttribute()]
    public static void SetSettingEncrypted( 
       [ISettingsManager](topic442.md) _this_ ,
       [SettingLevel](topic661.md) _level_ ,
       string _settingName_ ,
       string _settingValue_ ,
       bool _preventRedirection_
    )  
  
#### Parameters

 _this_
    The [ISettingsManager](topic442.md) to use to save the specified setting.
_level_
    The level at which to save the setting.
_settingName_
    The full name of the setting, e.g. "Common\MyValue".
_settingValue_
    The value to save.
_preventRedirection_
    True to prevent automatic redirection if redirection is turned on.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Extensions Class](topic814.md)   
[Extensions Members](topic815.md)

©2024 DriveWorks Ltd. All Rights Reserved.
