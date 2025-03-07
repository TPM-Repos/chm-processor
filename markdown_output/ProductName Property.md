Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProductName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectedClientDetails Class](topic2537.md) : ProductName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets or sets the name of the DriveWorks module that the client is connected to. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DataMemberAttribute()>
    Public Property ProductName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectedClientDetails](topic2537.md)
    Dim value As String
     
    instance.ProductName = value
     
    value = instance.ProductName  
  
C#|   
---|---  
      
    
    [DataMemberAttribute()]
    public string ProductName {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectedClientDetails Class](topic2537.md)   
[ConnectedClientDetails Members](topic2538.md)


