Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocuments Class](topic4434.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an enumerator which enumerates the documents in the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetEnumerator() As IEnumerator(Of ProjectDocument)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocuments](topic4434.md)
    Dim value As IEnumerator(Of ProjectDocument)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public IEnumerator<ProjectDocument> GetEnumerator()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocuments Class](topic4434.md)   
[ProjectDocuments Members](topic4435.md)


