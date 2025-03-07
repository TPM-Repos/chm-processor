Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSetting Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISettingsManager Interface](topic442.md) : GetSetting Method  
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

Glossary Item Box

Gets the specified setting. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetSetting( _
       ByVal _level_ As [SettingLevel](topic661.md), _
       ByVal _settingName_ As String, _
       ByVal _preventRedirection_ As Boolean _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISettingsManager](topic442.md)
    Dim level As [SettingLevel](topic661.md)
    Dim settingName As String
    Dim preventRedirection As Boolean
    Dim value As Object
     
    value = instance.GetSetting(level, settingName, preventRedirection)  
  
C#|   
---|---  
      
    
    object GetSetting( 
       [SettingLevel](topic661.md) _level_ ,
       string _settingName_ ,
       bool _preventRedirection_
    )  
  
#### Parameters

 _level_
    The level from which to load the setting.
_settingName_
    The full name of the setting, e.g. "Common\MyValue".
_preventRedirection_
    True to prevent automatic redirection if redirection is turned on.

#### Return Value

A null reference (Nothing in Visual Basic) if the setting doesn't exist, otherwise the value of the setting.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISettingsManager Interface](topic442.md)   
[ISettingsManager Members](topic443.md)


