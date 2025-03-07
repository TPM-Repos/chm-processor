Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CanEditCompletedSpecificationsCondition Class   
[Members](topic11838.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardConditions Namespace](topic11828.md) : CanEditCompletedSpecificationsCondition Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

A specification-flow condition which determines whether the ReleaseToAutoPilot is enabled. 

# Object Model

![](dotnetdiagramimages/image608.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[ConditionAttribute](topic10832.md)(DisplayName="resx://DriveWorks.ConditionsLocalizedResources,ConditionDispNameCanEditCompletedSpecificationsCondition", 
       Image="embedded://DriveWorks.DriveWorksSettingConditionPlain16.png", 
       WarningOutputEnabled=True)>
    Public Class CanEditCompletedSpecificationsCondition 
       Inherits [DriveWorks.Specification.Condition](topic10804.md)
       Implements [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CanEditCompletedSpecificationsCondition](topic11837.md)  
  
C#|   
---|---  
      
    
    [[ConditionAttribute](topic10832.md)(DisplayName="resx://DriveWorks.ConditionsLocalizedResources,ConditionDispNameCanEditCompletedSpecificationsCondition", 
       Image="embedded://DriveWorks.DriveWorksSettingConditionPlain16.png", 
       WarningOutputEnabled=true)]
    public class CanEditCompletedSpecificationsCondition : [DriveWorks.Specification.Condition](topic10804.md), [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md)  
[DriveWorks.Specification.Condition](topic10804.md)  
**DriveWorks.Specification.StandardConditions.CanEditCompletedSpecificationsCondition**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CanEditCompletedSpecificationsCondition Members](topic11838.md)   
[DriveWorks.Specification.StandardConditions Namespace](topic11828.md)


