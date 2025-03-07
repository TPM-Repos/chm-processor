Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Connect Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeNavigationInput Class](topic7058.md) : Connect Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_output_
    The condition output to map this input to.

Glossary Item Box

Create a connection between this input and the given [NodeOutput](topic7074.md), scheduling the [IFlowNode](topic6873.md) that owns this input to be executed if the mapped output is fulfilled during execution. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Sub Connect( _
       ByVal _output_ As [NodeOutput](topic7074.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeNavigationInput](topic7058.md)
    Dim output As [NodeOutput](topic7074.md)
     
    instance.Connect(output)  
  
C#|   
---|---  
      
    
    public override void Connect( 
       [NodeOutput](topic7074.md) _output_
    )  
  
#### Parameters

 _output_
    The condition output to map this input to.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| output is not a [ConditionOutput](topic6901.md) or a [NodeNavigationOutput](topic7067.md).  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeNavigationInput Class](topic7058.md)   
[NodeNavigationInput Members](topic7059.md)


