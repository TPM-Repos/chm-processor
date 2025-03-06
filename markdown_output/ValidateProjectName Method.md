ValidateProjectName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [ValidationUtility Class](topic13287.md) : ValidateProjectName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectName_
    

Glossary Item Box

Validates a DriveWorks Project name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ValidateProjectName( _
       ByVal _projectName_ As String _
    ) As [ValidateNameResult](topic13193.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim projectName As String
    Dim value As [ValidateNameResult](topic13193.md)
     
    value = [ValidationUtility](topic13287.md).ValidateProjectName(projectName)  
  
C#|   
---|---  
      
    
    public static [ValidateNameResult](topic13193.md) ValidateProjectName( 
       string _projectName_
    )  
  
#### Parameters

 _projectName_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ValidationUtility Class](topic13287.md)   
[ValidationUtility Members](topic13288.md)


