Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetParameterValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleaseParameterDataContainer Class](topic5145.md) : GetParameterValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the parameter whose calculated value to retrieve.

Glossary Item Box

Retrieves the value of the parameter with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetParameterValue( _
       ByVal _name_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseParameterDataContainer](topic5145.md)
    Dim name As String
    Dim value As String
     
    value = instance.GetParameterValue(name)  
  
C#|   
---|---  
      
    
    public string GetParameterValue( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the parameter whose calculated value to retrieve.

#### Return Value

This method returns null (Nothing in Visual Basic) if the parameter was not found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseParameterDataContainer Class](topic5145.md)   
[ReleaseParameterDataContainer Members](topic5146.md)


