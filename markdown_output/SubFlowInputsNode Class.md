       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SubFlowInputsNode Class   
[Members](topic7137.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7136.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) : SubFlowInputsNode Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

This node represents the inputs to a SubFlow. 

# Object Model

![](dotnetdiagramimages/image382.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[TaskAttribute](topic11659.md)(DisplayName="Inputs", 
       Image="", 
       CategoryName="", 
       WarningOutputEnabled=True)>
    Public Class SubFlowInputsNode 
       Inherits [DriveWorks.Specification.Task](topic11629.md)
       Implements [IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SubFlowInputsNode](topic7136.md)  
  
C#|   
---|---  
      
    
    [[TaskAttribute](topic11659.md)(DisplayName="Inputs", 
       Image="", 
       CategoryName="", 
       WarningOutputEnabled=true)]
    public class SubFlowInputsNode : [DriveWorks.Specification.Task](topic11629.md), [IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Remarks

Expose an input of a node in the SubFlow by making a connection to this node's last output.

# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md)  
[DriveWorks.EventFlow.ExecutableNodeWithStatus](topic6990.md)  
[DriveWorks.Specification.Task](topic11629.md)  
**DriveWorks.EventFlow.SubFlowInputsNode**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SubFlowInputsNode Members](topic7137.md)   
[DriveWorks.EventFlow Namespace](topic6871.md)

©2024 DriveWorks Ltd. All Rights Reserved.
