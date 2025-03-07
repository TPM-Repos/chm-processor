Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IProjectTemplateHelper Interface](topic2091.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_templatePath_
    The path to the template, or a null reference (Nothing in Visual Basic) if the template helper is standalone.

Glossary Item Box

Initializes the template helper with the path to the template. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Initialize( _
       ByVal _templatePath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProjectTemplateHelper](topic2091.md)
    Dim templatePath As String
     
    instance.Initialize(templatePath)  
  
C#|   
---|---  
      
    
    void Initialize( 
       string _templatePath_
    )  
  
#### Parameters

 _templatePath_
    The path to the template, or a null reference (Nothing in Visual Basic) if the template helper is standalone.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProjectTemplateHelper Interface](topic2091.md)   
[IProjectTemplateHelper Members](topic2092.md)


