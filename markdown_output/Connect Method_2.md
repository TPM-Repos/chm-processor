Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Connect Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [InputConnectionEndpoint Class](topic7033.md) : Connect Method  
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
      
    
    Public MustOverride Sub Connect( _
       ByVal _output_ As [NodeOutput](topic7074.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [InputConnectionEndpoint](topic7033.md)
    Dim output As [NodeOutput](topic7074.md)
     
    instance.Connect(output)  
  
C#|   
---|---  
      
    
    public abstract void Connect( 
       [NodeOutput](topic7074.md) _output_
    )  
  
#### Parameters

 _output_
    The output to map this input value to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[InputConnectionEndpoint Class](topic7033.md)   
[InputConnectionEndpoint Members](topic7034.md)


