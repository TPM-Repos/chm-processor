       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReleaseToAutopilotCondition Class   
[Members](topic6747.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks.StandardConditions Namespace](topic6735.md) : ReleaseToAutopilotCondition Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

A Component Task condition which determines whether the ReleaseToAutoPilot setting is turned on. 

# Object Model

![](dotnetdiagramimages/image355.png)

# Syntax

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
  
Visual Basic (Usage)| Copy Code  
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
  
# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.Components.Tasks.ComponentTaskReleaseCondition](topic6647.md)  
**DriveWorks.Components.Tasks.StandardConditions.ReleaseToAutopilotCondition**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseToAutopilotCondition Members](topic6747.md)   
[DriveWorks.Components.Tasks.StandardConditions Namespace](topic6735.md)


