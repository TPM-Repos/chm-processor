       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetParameter(String,ReleasedParameterData) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5071.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedComponentTask Class](topic5061.md) > [TryGetParameter Method](topic5070.md) : TryGetParameter(String,ReleasedParameterData) Method  
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
      
    
    Dim instance As [ReleasedComponentTask](topic5061.md)
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

[ReleasedComponentTask Class](topic5061.md)   
[ReleasedComponentTask Members](topic5062.md)   
[Overload List](topic5070.md)

©2024 DriveWorks Ltd. All Rights Reserved.
