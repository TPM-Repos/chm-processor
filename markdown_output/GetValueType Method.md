Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetValueType Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) : GetValueType Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value whose type is to be determined.

_throwOnError_
    

Glossary Item Box

Gets the store value type for the specified value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetValueType( _
       ByVal _value_ As Object, _
       ByVal _throwOnError_ As Boolean _
    ) As [StoreValueType](topic7322.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value As Object
    Dim throwOnError As Boolean
    Dim value As [StoreValueType](topic7322.md)
     
    value = [StoreConverter](topic9528.md).GetValueType(value, throwOnError)  
  
C#|   
---|---  
      
    
    public static [StoreValueType](topic7322.md) GetValueType( 
       object _value_ ,
       bool _throwOnError_
    )  
  
#### Parameters

 _value_
    The value whose type is to be determined.
_throwOnError_
    

#### Return Value

The store value type of the specified value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)


