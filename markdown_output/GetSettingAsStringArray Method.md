![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSettingAsStringArray Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic452.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISettingsManager Interface](topic442.md) : GetSettingAsStringArray Method  
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

Gets the specified setting as a string array. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetSettingAsStringArray( _
       ByVal _level_ As [SettingLevel](topic661.md), _
       ByVal _settingName_ As String, _
       ByVal _preventRedirection_ As Boolean _
    ) As String()  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISettingsManager](topic442.md)
    Dim level As [SettingLevel](topic661.md)
    Dim settingName As String
    Dim preventRedirection As Boolean
    Dim value() As String
     
    value = instance.GetSettingAsStringArray(level, settingName, preventRedirection)  
  
C#|   
---|---  
      
    
    string[] GetSettingAsStringArray( 
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISettingsManager Interface](topic442.md)   
[ISettingsManager Members](topic443.md)

©2024 DriveWorks Ltd. All Rights Reserved.
