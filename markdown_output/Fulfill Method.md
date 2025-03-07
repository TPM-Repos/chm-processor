Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Fulfill Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeOutput Class](topic7074.md) : Fulfill Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to assign to this output.

Glossary Item Box

Assign a static value to this input. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Sub Fulfill( _
       ByVal _value_ As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeOutput](topic7074.md)
    Dim value As Object
     
    instance.Fulfill(value)  
  
C#|   
---|---  
      
    
    public virtual void Fulfill( 
       object _value_
    )  
  
#### Parameters

 _value_
    The value to assign to this output.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeOutput Class](topic7074.md)   
[NodeOutput Members](topic7075.md)


