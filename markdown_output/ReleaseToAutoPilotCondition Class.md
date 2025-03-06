![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReleaseToAutopilotCondition Class   
[Members](topic6747.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6746.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks.StandardConditions Namespace](topic6735.md) : ReleaseToAutopilotCondition Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

A Component Task condition which determines whether the ReleaseToAutoPilot setting is turned on. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image355.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[ComponentTaskConditionAttribute](topic6512.md)(Title="resx://DriveWorks.ConditionsLocalizedResources,ConditionDispNameReleaseToAutoPilotCondition", 
       Description="resx://DriveWorks.ConditionsLocalizedResources,ConditionDescriptionReleaseToAutoPilot", 
       Image="embedded://DriveWorks.DriveWorksSettingConditionPlain16.png", 
       Category="resx://DriveWorks.ConditionsLocalizedResources,ConditionCategoryGeneral", 
       AllowedLocations=ComponentTaskSequenceLocation.PreCopy Or  _
        ComponentTaskSequenceLocation.PostCopy Or  _
        ComponentTaskSequenceLocation.Before Or  _
        ComponentTaskSequenceLocation.After Or  _
        ComponentTaskSequenceLocation.PostClose Or  _
        ComponentTaskSequenceLocation.PreClose Or  _
        ComponentTaskSequenceLocation.All)>
    Public Class ReleaseToAutopilotCondition 
       Inherits [DriveWorks.Components.Tasks.ComponentTaskReleaseCondition](topic6647.md)
       Implements [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleaseToAutopilotCondition](topic6746.md)  
  
C#|   
---|---  
      
    
    [[ComponentTaskConditionAttribute](topic6512.md)(Title="resx://DriveWorks.ConditionsLocalizedResources,ConditionDispNameReleaseToAutoPilotCondition", 
       Description="resx://DriveWorks.ConditionsLocalizedResources,ConditionDescriptionReleaseToAutoPilot", 
       Image="embedded://DriveWorks.DriveWorksSettingConditionPlain16.png", 
       Category="resx://DriveWorks.ConditionsLocalizedResources,ConditionCategoryGeneral", 
       AllowedLocations=ComponentTaskSequenceLocation.PreCopy | 
        ComponentTaskSequenceLocation.PostCopy | 
        ComponentTaskSequenceLocation.Before | 
        ComponentTaskSequenceLocation.After | 
        ComponentTaskSequenceLocation.PostClose | 
        ComponentTaskSequenceLocation.PreClose | 
        ComponentTaskSequenceLocation.All)]
    public class ReleaseToAutopilotCondition : [DriveWorks.Components.Tasks.ComponentTaskReleaseCondition](topic6647.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.Components.Tasks.ComponentTaskReleaseCondition](topic6647.md)  
**DriveWorks.Components.Tasks.StandardConditions.ReleaseToAutopilotCondition**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleaseToAutopilotCondition Members](topic6747.md)   
[DriveWorks.Components.Tasks.StandardConditions Namespace](topic6735.md)

©2024 DriveWorks Ltd. All Rights Reserved.
