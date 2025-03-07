Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsDriveApp Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationEnvironment Class](topic11355.md) : IsDriveApp Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets whether or not the specification is an instance of a DriveApp. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property IsDriveApp As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationEnvironment](topic11355.md)
    Dim value As Boolean
     
    value = instance.IsDriveApp  
  
C#|   
---|---  
      
    
    public bool IsDriveApp {get;}  
  
# Remarks

This is only True if [DriveAppId](topic11365.md) has a value.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationEnvironment Class](topic11355.md)   
[SpecificationEnvironment Members](topic11356.md)


