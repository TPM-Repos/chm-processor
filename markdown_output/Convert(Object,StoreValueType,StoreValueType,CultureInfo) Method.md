Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Convert(Object,StoreValueType,StoreValueType,CultureInfo) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) > [Convert Method](topic9534.md) : Convert(Object,StoreValueType,StoreValueType,CultureInfo) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to convert.

_sourceType_
    The source type of the value.

_destinationType_
    The destination type.

_culture_
    An instance of the System.Globalization.CultureInfo defining how culture-specific conversions should be performed.

Glossary Item Box

Converts the specified value from its current type to the specified type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Convert( _
       ByVal _value_ As Object, _
       ByVal _sourceType_ As [StoreValueType](topic7322.md), _
       ByVal _destinationType_ As [StoreValueType](topic7322.md), _
       ByVal _culture_ As CultureInfo _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value As Object
    Dim sourceType As [StoreValueType](topic7322.md)
    Dim destinationType As [StoreValueType](topic7322.md)
    Dim culture As CultureInfo
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).Convert(value, sourceType, destinationType, culture)  
  
C#|   
---|---  
      
    
    public static object Convert( 
       object _value_ ,
       [StoreValueType](topic7322.md) _sourceType_ ,
       [StoreValueType](topic7322.md) _destinationType_ ,
       CultureInfo _culture_
    )  
  
#### Parameters

 _value_
    The value to convert.
_sourceType_
    The source type of the value.
_destinationType_
    The destination type.
_culture_
    An instance of the System.Globalization.CultureInfo defining how culture-specific conversions should be performed.

#### Return Value

The converted value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)   
[Overload List](topic9534.md)


