![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SettingChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3021.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : SettingChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a setting is changed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event SettingChanged As EventHandler(Of SettingChangedEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim handler As EventHandler(Of SettingChangedEventArgs)
     
    AddHandler instance.SettingChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SettingChangedEventArgs> SettingChanged  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [SettingChangedEventArgs](topic5288.md) containing data related to this event. The following **SettingChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[SettingName](topic5296.md)| Gets the name of the setting that was changed.   
[SettingValue](topic5297.md)| Gets the new value of the setting that was changed.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)

©2024 DriveWorks Ltd. All Rights Reserved.
