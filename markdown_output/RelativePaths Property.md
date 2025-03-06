       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RelativePaths Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10786.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [AdditionalFoldersCreatedEventArgs Class](topic10775.md) : RelativePaths Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the relative paths of the additional folders that were created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property RelativePaths As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [AdditionalFoldersCreatedEventArgs](topic10775.md)
    Dim value() As String
     
    value = instance.RelativePaths  
  
C#|   
---|---  
      
    
    public string[] RelativePaths {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AdditionalFoldersCreatedEventArgs Class](topic10775.md)   
[AdditionalFoldersCreatedEventArgs Members](topic10776.md)

©2024 DriveWorks Ltd. All Rights Reserved.
