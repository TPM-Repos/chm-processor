Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DocumentDesignerAttribute Class   
[Members](topic1569.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md) : DocumentDesignerAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Applied to a class implementing the [IDocumentDesigner](topic1517.md) interface to provide information about the document designer. 

# Object Model

![](dotnetdiagramimages/image56.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=False, 
       Inherited=True)>
    Public Class DocumentDesignerAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DocumentDesignerAttribute](topic1568.md)  
  
C#|   
---|---  
      
    
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=false, 
       Inherited=true)]
    public class DocumentDesignerAttribute : System.Attribute   
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.Applications.Administrator.Extensibility.Documents.DocumentDesignerAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DocumentDesignerAttribute Members](topic1569.md)   
[DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md)


