Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetFiles Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [FilePickingOptions Class](topic9902.md) : GetFiles Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an effective collection of all files that are included based on the current options. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetFiles() As HashSet(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FilePickingOptions](topic9902.md)
    Dim value As HashSet(Of String)
     
    value = instance.GetFiles()  
  
C#|   
---|---  
      
    
    public HashSet<string> GetFiles()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FilePickingOptions Class](topic9902.md)   
[FilePickingOptions Members](topic9903.md)


