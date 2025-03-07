Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Convert(Object,StoreValueType) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) > [Convert Method](topic9534.md) : Convert(Object,StoreValueType) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to convert.

_destinationType_
    The destination type.

Glossary Item Box

Converts the specified value from its current type to the specified type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Convert( _
       ByVal _value_ As Object, _
       ByVal _destinationType_ As [StoreValueType](topic7322.md) _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value As Object
    Dim destinationType As [StoreValueType](topic7322.md)
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).Convert(value, destinationType)  
  
C#|   
---|---  
      
    
    public static object Convert( 
       object _value_ ,
       [StoreValueType](topic7322.md) _destinationType_
    )  
  
#### Parameters

 _value_
    The value to convert.
_destinationType_
    The destination type.

#### Return Value

The converted value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)   
[Overload List](topic9534.md)


