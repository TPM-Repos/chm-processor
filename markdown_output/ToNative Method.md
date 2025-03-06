ToNative Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [IPropertyValueConverter Interface](topic9373.md) : ToNative Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value from the backing store.

Glossary Item Box

Takes the value from the backing store and converts it to its native type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ToNative( _
       ByVal _value_ As Object _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPropertyValueConverter](topic9373.md)
    Dim value As Object
    Dim value As Object
     
    value = instance.ToNative(value)  
  
C#|   
---|---  
      
    
    object ToNative( 
       object _value_
    )  
  
#### Parameters

 _value_
    The value from the backing store.

#### Return Value

A value of the native type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPropertyValueConverter Interface](topic9373.md)   
[IPropertyValueConverter Members](topic9374.md)


