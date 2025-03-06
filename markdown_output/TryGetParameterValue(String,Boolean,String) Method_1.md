TryGetParameterValue(String,Boolean,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleaseParameterDataContainer Class](topic5145.md) > [TryGetParameterValue Method](topic5156.md) : TryGetParameterValue(String,Boolean,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter whose calculated value to retrieve.

_failOnEmptyString_
    True if this method should return false if the value is found, but is an empty string.

_value_
    The calculated value of the parameter if the parameter was found.

Glossary Item Box

Attempts to retrieve the value of the parameter with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetParameterValue( _
       ByVal _name_ As String, _
       ByVal _failOnEmptyString_ As Boolean, _
       ByRef _value_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseParameterDataContainer](topic5145.md)
    Dim name As String
    Dim failOnEmptyString As Boolean
    Dim value As String
    Dim value As Boolean
     
    value = instance.TryGetParameterValue(name, failOnEmptyString, value)  
  
C#|   
---|---  
      
    
    public bool TryGetParameterValue( 
       string _name_ ,
       bool _failOnEmptyString_ ,
       ref string _value_
    )  
  
#### Parameters

 _name_
    The name of the parameter whose calculated value to retrieve.
_failOnEmptyString_
    True if this method should return false if the value is found, but is an empty string.
_value_
    The calculated value of the parameter if the parameter was found.

#### Return Value

True if the parameter was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseParameterDataContainer Class](topic5145.md)   
[ReleaseParameterDataContainer Members](topic5146.md)   
[Overload List](topic5156.md)


