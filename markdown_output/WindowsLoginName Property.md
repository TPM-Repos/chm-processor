       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
WindowsLoginName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectedClientDetails Class](topic2537.md) : WindowsLoginName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets or sets the windows username that the client is logged in as. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DataMemberAttribute()>
    Public Property WindowsLoginName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectedClientDetails](topic2537.md)
    Dim value As String
     
    instance.WindowsLoginName = value
     
    value = instance.WindowsLoginName  
  
C#|   
---|---  
      
    
    [DataMemberAttribute()]
    public string WindowsLoginName {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectedClientDetails Class](topic2537.md)   
[ConnectedClientDetails Members](topic2538.md)


