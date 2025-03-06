       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ToStore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [PropertyValueConverterBase Class](topic9489.md) : ToStore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function ToStore( _
       ByVal _value_ As Object _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PropertyValueConverterBase](topic9489.md)
    Dim value As Object
    Dim value As Object
     
    value = instance.ToStore(value)  
  
C#|   
---|---  
      
    
    public abstract object ToStore( 
       object _value_
    )  
  
#### Parameters

 _value_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PropertyValueConverterBase Class](topic9489.md)   
[PropertyValueConverterBase Members](topic9490.md)


