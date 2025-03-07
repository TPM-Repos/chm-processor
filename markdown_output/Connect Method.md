Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Connect Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperty Class](topic10946.md) : Connect Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_output_
    The output to map this input value to.

Glossary Item Box

Connects this input to the given output. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Sub Connect( _
       ByVal _output_ As [NodeOutput](topic7074.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowProperty](topic10946.md)
    Dim output As [NodeOutput](topic7074.md)
     
    instance.Connect(output)  
  
C#|   
---|---  
      
    
    public override void Connect( 
       [NodeOutput](topic7074.md) _output_
    )  
  
#### Parameters

 _output_
    The output to map this input value to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowProperty Class](topic10946.md)   
[FlowProperty Members](topic10947.md)


