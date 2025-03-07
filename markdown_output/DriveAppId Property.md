Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveAppId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationEnvironment Class](topic11355.md) : DriveAppId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the optional unique identifier of the DriveApp instance that this specification represents. This has no value if the [SpecificationEnvironment](topic11355.md) is not for a DriveApp. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property DriveAppId As Nullable(Of Guid)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationEnvironment](topic11355.md)
    Dim value As Nullable(Of Guid)
     
    instance.DriveAppId = value
     
    value = instance.DriveAppId  
  
C#|   
---|---  
      
    
    public Nullable<Guid> DriveAppId {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationEnvironment Class](topic11355.md)   
[SpecificationEnvironment Members](topic11356.md)


