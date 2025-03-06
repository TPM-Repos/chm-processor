TryGetParameter(String,ReleasedParameterData) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleaseParameterDataContainer Class](topic5145.md) > [TryGetParameter Method](topic5153.md) : TryGetParameter(String,ReleasedParameterData) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter to get.

_parameter_
    The parameter if it was found.

Glossary Item Box

Attempts to get the parameter data that matches the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetParameter( _
       ByVal _name_ As String, _
       ByRef _parameter_ As ReleasedParameterData _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseParameterDataContainer](topic5145.md)
    Dim name As String
    Dim parameter As ReleasedParameterData
    Dim value As Boolean
     
    value = instance.TryGetParameter(name, parameter)  
  
C#|   
---|---  
      
    
    public bool TryGetParameter( 
       string _name_ ,
       ref ReleasedParameterData _parameter_
    )  
  
#### Parameters

 _name_
    The name of the parameter to get.
_parameter_
    The parameter if it was found.

#### Return Value

True if the parameter was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseParameterDataContainer Class](topic5145.md)   
[ReleaseParameterDataContainer Members](topic5146.md)   
[Overload List](topic5153.md)


