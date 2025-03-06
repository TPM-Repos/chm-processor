       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetParameter(String,Boolean,ReleasedParameterData) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5155.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleaseParameterDataContainer Class](topic5145.md) > [TryGetParameter Method](topic5153.md) : TryGetParameter(String,Boolean,ReleasedParameterData) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter to get.

_excludeEmpty_
    True if an empty parameter value should be considered non-existent.

_parameter_
    The parameter if it was found.

Glossary Item Box

Attempts to get the paramter data that matches the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetParameter( _
       ByVal _name_ As String, _
       ByVal _excludeEmpty_ As Boolean, _
       ByRef _parameter_ As ReleasedParameterData _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseParameterDataContainer](topic5145.md)
    Dim name As String
    Dim excludeEmpty As Boolean
    Dim parameter As ReleasedParameterData
    Dim value As Boolean
     
    value = instance.TryGetParameter(name, excludeEmpty, parameter)  
  
C#|   
---|---  
      
    
    public bool TryGetParameter( 
       string _name_ ,
       bool _excludeEmpty_ ,
       ref ReleasedParameterData _parameter_
    )  
  
#### Parameters

 _name_
    The name of the parameter to get.
_excludeEmpty_
    True if an empty parameter value should be considered non-existent.
_parameter_
    The parameter if it was found.

#### Return Value

True if the parameter was found. If excludeEmpty is True then returns whether the parameter was found and it's value was not empty.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseParameterDataContainer Class](topic5145.md)   
[ReleaseParameterDataContainer Members](topic5146.md)   
[Overload List](topic5153.md)

©2024 DriveWorks Ltd. All Rights Reserved.
