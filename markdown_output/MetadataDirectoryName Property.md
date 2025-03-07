Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MetadataDirectoryName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : MetadataDirectoryName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the name of a directory which will act as a container for artifacts used to manage a specification, or a null reference to put them in the specification folder. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property MetadataDirectoryName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As String
     
    value = instance.MetadataDirectoryName  
  
C#|   
---|---  
      
    
    public string MetadataDirectoryName {get;}  
  
# Remarks

DriveWorks supports the notion of a metadata directory which is a directory inside the specification directory in which the design master, project file, and related metadata are stored. If used, this feature prevents the specification directory from becoming cluttered with information which DriveWorks uses to manage the specification.

If the metadirectory name is zero-length or a null reference (Nothing in Visual Basic), then DriveWorks will place metadata files in the specification directory.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


