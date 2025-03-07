Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GroupLoginName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectedClientDetails Class](topic2537.md) : GroupLoginName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets or sets the username that is currently logged in to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DataMemberAttribute()>
    Public Property GroupLoginName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectedClientDetails](topic2537.md)
    Dim value As String
     
    instance.GroupLoginName = value
     
    value = instance.GroupLoginName  
  
C#|   
---|---  
      
    
    [DataMemberAttribute()]
    public string GroupLoginName {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectedClientDetails Class](topic2537.md)   
[ConnectedClientDetails Members](topic2538.md)


