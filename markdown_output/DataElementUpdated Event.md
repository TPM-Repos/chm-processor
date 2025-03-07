Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DataElementUpdated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMetadataSection Class](topic4654.md) : DataElementUpdated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when [DataElement](topic4660.md) has been set to a new System.Xml.Linq.XElement. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event DataElementUpdated As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectMetadataSection](topic4654.md)
    Dim handler As EventHandler
     
    AddHandler instance.DataElementUpdated, handler  
  
C#|   
---|---  
      
    
    public event EventHandler DataElementUpdated  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMetadataSection Class](topic4654.md)   
[ProjectMetadataSection Members](topic4655.md)


