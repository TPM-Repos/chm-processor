Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertFromObject Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperty<T> Class](topic10978.md) : ConvertFromObject Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function ConvertFromObject( _
       ByVal _value_ As Object _
    ) As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowProperty(Of T)](topic10978.md)
    Dim value As Object
    Dim value As T
     
    value = instance.ConvertFromObject(value)  
  
C#|   
---|---  
      
    
    protected virtual T ConvertFromObject( 
       object _value_
    )  
  
#### Parameters

 _value_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowProperty<T> Class](topic10978.md)   
[FlowProperty<T> Members](topic10979.md)


