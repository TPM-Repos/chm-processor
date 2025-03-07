Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DocumentsRelativeToSpecificationFolder Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationSettings Class](topic4885.md) : DocumentsRelativeToSpecificationFolder Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether documents' paths are calculated relative to the specification's folder, if false, they are calculated relative to the default specification folder instead. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property DocumentsRelativeToSpecificationFolder As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationSettings](topic4885.md)
    Dim value As Boolean
     
    instance.DocumentsRelativeToSpecificationFolder = value
     
    value = instance.DocumentsRelativeToSpecificationFolder  
  
C#|   
---|---  
      
    
    public bool DocumentsRelativeToSpecificationFolder {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecificationSettings Class](topic4885.md)   
[ProjectSpecificationSettings Members](topic4886.md)


