       

_T_
    The type to convert the released parameter value to.

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetParameterValue<T>(String,Boolean,T) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleaseParameterDataContainer Class](topic5145.md) > [TryGetParameterValue Method](topic5156.md) : TryGetParameterValue<T>(String,Boolean,T) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter whose calculated value to retrieve.

_failOnEmptyString_
    True if this method should return false if the value is found, but is an empty string before conversion.

_value_
    The calculated value of the parameter if the parameter was found.

Glossary Item Box

Attempts to retrieve the value of the parameter with the given name as T. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetParameterValue(Of T As {New, Struct})( _
       ByVal _name_ As String, _
       ByVal _failOnEmptyString_ As Boolean, _
       ByRef _value_ As T _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseParameterDataContainer](topic5145.md)
    Dim name As String
    Dim failOnEmptyString As Boolean
    Dim value As T
    Dim value As Boolean
     
    value = instance.TryGetParameterValue(Of T)(name, failOnEmptyString, value)  
  
C#|   
---|---  
      
    
    public bool TryGetParameterValue<T>( 
       string _name_ ,
       bool _failOnEmptyString_ ,
       ref T _value_
    )
    where T: new(), struct  
  
#### Parameters

 _name_
    The name of the parameter whose calculated value to retrieve.
_failOnEmptyString_
    True if this method should return false if the value is found, but is an empty string before conversion.
_value_
    The calculated value of the parameter if the parameter was found.

#### Type Parameters

_T_
    The type to convert the released parameter value to.

#### Return Value

True if the parameter was found and it's value could successfully be converted to a T.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseParameterDataContainer Class](topic5145.md)   
[ReleaseParameterDataContainer Members](topic5146.md)   
[Overload List](topic5156.md)


