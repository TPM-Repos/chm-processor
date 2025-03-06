ToStore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [IPropertyValueConverter Interface](topic9373.md) : ToStore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The native value to convert.

Glossary Item Box

Takes a native value, and converts it to one of the types understood by the backing store. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ToStore( _
       ByVal _value_ As Object _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPropertyValueConverter](topic9373.md)
    Dim value As Object
    Dim value As Object
     
    value = instance.ToStore(value)  
  
C#|   
---|---  
      
    
    object ToStore( 
       object _value_
    )  
  
#### Parameters

 _value_
    The native value to convert.

#### Return Value

A value in one of the types understood by the backing store.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPropertyValueConverter Interface](topic9373.md)   
[IPropertyValueConverter Members](topic9374.md)


