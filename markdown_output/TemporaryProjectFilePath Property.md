       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TemporaryProjectFilePath Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11235.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : TemporaryProjectFilePath Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the fully-qualified path to the context's temporary copy of the project file. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property TemporaryProjectFilePath As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As String
     
    value = instance.TemporaryProjectFilePath  
  
C#|   
---|---  
      
    
    public string TemporaryProjectFilePath {get;}  
  
#### Property Value

The fully-qualified path to the context's temporary copy of the project file if the context is in a running state, otherwise, a null reference (Nothing in Visual Basic).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)

©2024 DriveWorks Ltd. All Rights Reserved.
