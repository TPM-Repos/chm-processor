![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SettingValueChangedEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic982.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [SettingValueChangedEventArgs Class](topic975.md) : SettingValueChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_settingName_
    The name of the setting whose value was changed.

_settingValue_
    The new value of the setting.

Glossary Item Box

Creates a new instance of the [SettingValueChangedEventArgs](topic975.md) event args. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _settingName_ As String, _
       ByVal _settingValue_ As Object _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim settingName As String
    Dim settingValue As Object
     
    Dim instance As New [SettingValueChangedEventArgs](topic975.md)(settingName, settingValue)  
  
C#|   
---|---  
      
    
    public SettingValueChangedEventArgs( 
       string _settingName_ ,
       object _settingValue_
    )  
  
#### Parameters

 _settingName_
    The name of the setting whose value was changed.
_settingValue_
    The new value of the setting.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SettingValueChangedEventArgs Class](topic975.md)   
[SettingValueChangedEventArgs Members](topic976.md)

©2024 DriveWorks Ltd. All Rights Reserved.
