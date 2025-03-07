Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertToString Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperty<T> Class](topic10978.md) : ConvertToString Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Function ConvertToString( _
       ByVal _value_ As T _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowProperty(Of T)](topic10978.md)
    Dim value As T
    Dim value As String
     
    value = instance.ConvertToString(value)  
  
C#|   
---|---  
      
    
    protected abstract string ConvertToString( 
       T _value_
    )  
  
#### Parameters

 _value_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowProperty<T> Class](topic10978.md)   
[FlowProperty<T> Members](topic10979.md)


