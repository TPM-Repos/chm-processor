Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileDocumentBase Class   
[Members](topic2871.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : FileDocumentBase Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a base for documents that are based on using specific files. 

# Object Model

![](dotnetdiagramimages/image119.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class FileDocumentBase 
       Inherits [ProjectDocument](topic4356.md)
       Implements [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileDocumentBase](topic2870.md)  
  
C#|   
---|---  
      
    
    public abstract class FileDocumentBase : [ProjectDocument](topic4356.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.ProjectDocument](topic4356.md)  
**DriveWorks.FileDocumentBase**  
[DriveWorks.AdvancedXmlDocument](topic2364.md)  
[DriveWorks.CopiedFile](topic2606.md)  
[DriveWorks.ExcelDocument](topic2834.md)  
[DriveWorks.JsonDocument](topic3635.md)  
[DriveWorks.WordDocument](topic5885.md)  
[DriveWorks.XmlTemplateDocument](topic5909.md)  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileDocumentBase Members](topic2871.md)   
[DriveWorks Namespace](topic2159.md)


