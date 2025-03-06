       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationBasePath Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11374.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationEnvironment Class](topic11355.md) : SpecificationBasePath Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the base path for specification files (this is usually equivalent to the group's default specification folder). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property SpecificationBasePath As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationEnvironment](topic11355.md)
    Dim value As String
     
    instance.SpecificationBasePath = value
     
    value = instance.SpecificationBasePath  
  
C#|   
---|---  
      
    
    public string SpecificationBasePath {get; set;}  
  
# Remarks

This property is usually initialized using the [DriveWorks.Group.DefaultSpecificationFolder](topic2999.md) property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationEnvironment Class](topic11355.md)   
[SpecificationEnvironment Members](topic11356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
