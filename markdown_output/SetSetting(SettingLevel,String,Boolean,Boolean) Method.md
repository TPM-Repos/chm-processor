SetSetting(SettingLevel,String,Boolean,Boolean) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISettingsManager Interface](topic442.md) > [SetSetting Method](topic454.md) : SetSetting(SettingLevel,String,Boolean,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

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
      
    
    Overloads Sub SetSetting( _
       ByVal _level_ As [SettingLevel](topic661.md), _
       ByVal _settingName_ As String, _
       ByVal _settingValue_ As Boolean, _
       ByVal _preventRedirection_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISettingsManager](topic442.md)
    Dim level As [SettingLevel](topic661.md)
    Dim settingName As String
    Dim settingValue As Boolean
    Dim preventRedirection As Boolean
     
    instance.SetSetting(level, settingName, settingValue, preventRedirection)  
  
C#|   
---|---  
      
    
    void SetSetting( 
       [SettingLevel](topic661.md) _level_ ,
       string _settingName_ ,
       bool _settingValue_ ,
       bool _preventRedirection_
    )  
  
#### Parameters

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

[ISettingsManager Interface](topic442.md)   
[ISettingsManager Members](topic443.md)   
[Overload List](topic454.md)


