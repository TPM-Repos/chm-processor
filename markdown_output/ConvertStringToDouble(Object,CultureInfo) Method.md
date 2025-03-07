Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertStringToDouble(Object,CultureInfo) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) > [ConvertStringToDouble Method](topic9556.md) : ConvertStringToDouble(Object,CultureInfo) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The source value.

_culture_
    An instance of the System.Globalization.CultureInfo defining how culture-specific conversions should be performed.

Glossary Item Box

Converts the specified string to a double. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function ConvertStringToDouble( _
       ByVal _value_ As Object, _
       ByVal _culture_ As CultureInfo _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value As Object
    Dim culture As CultureInfo
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).ConvertStringToDouble(value, culture)  
  
C#|   
---|---  
      
    
    public static object ConvertStringToDouble( 
       object _value_ ,
       CultureInfo _culture_
    )  
  
#### Parameters

 _value_
    The source value.
_culture_
    An instance of the System.Globalization.CultureInfo defining how culture-specific conversions should be performed.

#### Return Value

A double.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)   
[Overload List](topic9556.md)


