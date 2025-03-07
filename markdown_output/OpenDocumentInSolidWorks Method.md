Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OpenDocumentInSolidWorks Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ICaptureViewHost Interface](topic13363.md) : OpenDocumentInSolidWorks Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentPath_
    The path to the component to open.

Glossary Item Box

Opens the component with the given path in SolidWorks. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub OpenDocumentInSolidWorks( _
       ByVal _componentPath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICaptureViewHost](topic13363.md)
    Dim componentPath As String
     
    instance.OpenDocumentInSolidWorks(componentPath)  
  
C#|   
---|---  
      
    
    void OpenDocumentInSolidWorks( 
       string _componentPath_
    )  
  
#### Parameters

 _componentPath_
    The path to the component to open.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICaptureViewHost Interface](topic13363.md)   
[ICaptureViewHost Members](topic13364.md)


