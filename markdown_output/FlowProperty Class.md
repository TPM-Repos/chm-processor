Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FlowProperty Class   
[Members](topic10947.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : FlowProperty Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents an untyped property on a condition or task. 

# Object Model

![](dotnetdiagramimages/image555.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class FlowProperty 
       Inherits [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md)
       Implements [DriveWorks.Abstractions.IHasRule](topic5947.md), [DriveWorks.Abstractions.IHasRuleId](topic5957.md), [DriveWorks.Abstractions.IHasRuleType](topic5969.md), [DriveWorks.Abstractions.IHasRuleVersionHistory](topic5975.md), Titan.Rules.Execution.IHasCustomName   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowProperty](topic10946.md)  
  
C#|   
---|---  
      
    
    public abstract class FlowProperty : [DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md), [DriveWorks.Abstractions.IHasRule](topic5947.md), [DriveWorks.Abstractions.IHasRuleId](topic5957.md), [DriveWorks.Abstractions.IHasRuleType](topic5969.md), [DriveWorks.Abstractions.IHasRuleVersionHistory](topic5975.md), Titan.Rules.Execution.IHasCustomName    
  
# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.EventFlow.ConnectionEndpoint](topic6918.md)  
[DriveWorks.EventFlow.InputConnectionEndpoint](topic7033.md)  
**DriveWorks.Specification.FlowProperty**  
[DriveWorks.Specification.FlowProperty<T>](topic10978.md)  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowProperty Members](topic10947.md)   
[DriveWorks.Specification Namespace](topic10764.md)


