Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsCancellingCondition Class   
[Members](topic11865.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardConditions Namespace](topic11828.md) : IsCancellingCondition Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

A specification-flow condition which checks whether a specification is being cancelled. 

# Object Model

![](dotnetdiagramimages/image612.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[ConditionAttribute](topic10832.md)(DisplayName="resx://DriveWorks.ConditionsLocalizedResources,ConditionDispNameIsCancellingCondition", 
       Image="embedded://DriveWorks.IsCancellingPlain16.png", 
       WarningOutputEnabled=True)>
    Public Class IsCancellingCondition 
       Inherits [DriveWorks.Specification.Condition](topic10804.md)
       Implements [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IsCancellingCondition](topic11864.md)  
  
C#|   
---|---  
      
    
    [[ConditionAttribute](topic10832.md)(DisplayName="resx://DriveWorks.ConditionsLocalizedResources,ConditionDispNameIsCancellingCondition", 
       Image="embedded://DriveWorks.IsCancellingPlain16.png", 
       WarningOutputEnabled=true)]
    public class IsCancellingCondition : [DriveWorks.Specification.Condition](topic10804.md), [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md)  
[DriveWorks.Specification.Condition](topic10804.md)  
**DriveWorks.Specification.StandardConditions.IsCancellingCondition**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IsCancellingCondition Members](topic11865.md)   
[DriveWorks.Specification.StandardConditions Namespace](topic11828.md)


